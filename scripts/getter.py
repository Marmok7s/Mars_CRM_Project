import sqlite3


def get_cursor(database):
    data = sqlite3.connect(database)
    cur = data.cursor()
    return cur


def get_clients(database):
    cur = get_cursor(database)
    clients = cur.execute("SELECT * FROM clients").fetchall()
    return clients


def get_orders(database):
    cur = get_cursor(database)
    orders = cur.execute("SELECT * FROM orders").fetchall()
    return orders


def get_readable_orders(database):
    orders = get_orders(database)
    cur = get_cursor(database)
    for order in orders:
        order = list(order)
        client = cur.execute(f"SELECT name AND surname FROM clients WHERE id == {order[1]}").fetchone()
        order[1] = client[0]
        items = []
        for item in str(order[2]).split(" "):
            one = cur.execute(f"SELECT name FROM items WHERE id == {int(item)}").fetchone()
            items.append(one[0])
        order[2] = items
        if bool(order[4]):
            order[4] = 'Paid'
        else:
            order[4] = 'NotPaid'
    return orders


def get_jobs(database):
    cur = get_cursor(database)
    jobs = cur.execute("SELECT * FROM jobs").fetchall()
    return jobs


def get_readable_jobs(database):
    jobs = get_jobs(database)
    cur = get_cursor(database)
    for job in jobs:
        job = list(job)
        team_leader = cur.execute(f"SELECT name AND surname FROM users WHERE id == {int(job[2])}").fetchone()
        job[2] = team_leader[0]
        collaborators = []
        for collaborator in str(job[3]).split(' '):
            one = cur.execute(f"SELECT name AND surname FROM users WHERE id == {int(collaborator)}").fetchone()
            collaborators.append(one[0])
        job[3] = collaborators
        if bool(job[7]):
            job[7] = 'Finished'
        else:
            job[7] = 'Have not finished yet'
    return jobs


def get_data(database, table_name):
    cur = get_cursor(database)
    data = cur.execute(f"SELECT * FROM {str(table_name).lower()}").fetchall()
    return data

