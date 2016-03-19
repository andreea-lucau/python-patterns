"""Sample usage of the Mediator pattern."""
#!/usr/bin/env python
# pylint: disable=missing-docstring,too-few-public-methods

import random


class InvalidAccess(Exception):
    pass


class Mediator(object):

    def __init__(self):
        self.users = []
        self.depots = {
        }

    def add_user(self, user):
        user.mediator = self
        self.users.append(user)

    def add_depot(self, depot):
        self.depots[depot.name] = depot

    def check_permissions(self, user, depot):
        selected_depot = self._get_depot(depot)
        if selected_depot.restricted and not user.admin:
            raise InvalidAccess(
                "User %s cannot check depot %s", user.name, depot)
        else:
            return selected_depot.permissions

    def change_permissions(self, user, depot, permissions):
        selected_depot = self._get_depot(depot)
        if selected_depot.restricted and not user.admin:
            raise InvalidAccess(
                "User %s cannot change depot %s", user.name, depot)
        else:
            return selected_depot.change_permissions(permissions)

    def _get_depot(self, depot):
        selected_depot = self.depots.get(depot)
        if not selected_depot:
            raise InvalidAccess(
                "Users can't check depot %s, the depot does not exist" % (
                    depot))

        return selected_depot


class User(object):

    def __init__(self, name, admin=False):
        self.name = name
        self.admin = admin
        self.mediator = None

    def check_permissions(self, depot):
        return self.mediator.check_permissions(self, depot)

    def change_permissions(self, depot, permissions):
        self.mediator.change_permissions(self, depot, permissions)


class Depot(object):

    def __init__(self, name, permissions, restricted=False):
        self.name = name
        self.permissions = permissions
        self.restricted = restricted

    def change_permissions(self, permissions):
        self.permissions = permissions


def change_depots():
    mediator = Mediator()

    users = []
    users.append(User("alice", admin=True))
    users.append(User("bob", admin=True))
    users.append(User("truddy"))
    users.append(User("john"))

    depots = []
    depots.append(Depot("Src", "wr-", restricted=True))
    depots.append(Depot("Bin", "--e", restricted=True))
    depots.append(Depot("Docs", "rw-"))
    depots.append(Depot("Movies", "rw-"))

    for user in users:
        mediator.add_user(user)

    for depot in depots:
        mediator.add_depot(depot)

    permissions = ["-", "r", "w", "e",]

    for _ in range(10):
        user = users[random.randint(0, len(users) - 1)]
        depot = depots[random.randint(0, len(depots) - 1)]
        if random.randint(0, 1) == 0:
            print "User %s checked permissions for depot %s. " % (
                user.name, depot.name),
            try:
                depot_permissions = user.check_permissions(depot.name)
            except InvalidAccess:
                print "Invalid operation"
                continue

            print "Permissions:", depot_permissions
        else:
            new_permissions = "".join([
                permissions[random.randint(0, len(permissions) - 1)]
                for _ in range(3)
            ])
            print "User %s will change permissions for depot %s to %s." % (
                user.name, depot.name, new_permissions),

            try:
                user.change_permissions(depot.name, new_permissions)
            except InvalidAccess:
                print "Invalid operation"
                continue

            print ""


if __name__ == "__main__":
    change_depots()
