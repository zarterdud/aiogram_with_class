import sqlite3


class DataBase:
    def __init__(self, name_db):
        self.con = sqlite3.connect(name_db)
        self.cur = self.con.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS send_message(
                id INTEGER PRIMARY KEY,
                id_name INTEGER,
                id_message TEXT,
                question TEXT
            )
            """
        )
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS ls_tasks(
                id INTEGER PRIMARY KEY,
                tg_id INTEGER,
                id_task TEXT,
                id_theory TEXT,
                id_file TEXT,
                section TEXT,
                subsection TEXT
            )
            """
        )
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY,
                section TEXT,
                subsection TEXT,
                task_id INTEGER,
                theory_id INTEGER,
                file_id INTEGER
            )
            """
        )
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS tg_users(
                tg_id INTEGER,
                fullname TEXT,
                username TEXT,
                count_limit_message INTEGER
            )
            """
        )
        self.con.commit()

    def give_count_messages(self, tg_id):
        self.cur.execute(
            f"Update tg_users set count_limit_message = 5 where tg_id = {tg_id}"
        )
        self.con.commit()

    def take_away_count_messages(self, tg_id):
        count = self.cur.execute(
            f"SELECT count_limit_message FROM tg_users WHERE tg_id = {tg_id}"
        ).fetchall()[0][0]
        self.cur.execute(
            f"Update tg_users set count_limit_message = {count - 1} where tg_id = {tg_id}"
        )
        self.con.commit()

    def know_count_messages(self, tg_id):
        count = self.cur.execute(
            f"SELECT count_limit_message FROM tg_users WHERE tg_id = {tg_id}"
        ).fetchall()[0][0]
        return count

    def users_id(self):
        ids = self.cur.execute(f"SELECT tg_id FROM tg_users").fetchall()
        id_ret = []
        for user_id in ids:
            user_id = user_id[0]
            id_ret.append(user_id)
        return id_ret

    def user_in_db(self, id_user, name, username):
        self.cur.execute(
            f"INSERT INTO tg_users (tg_id, fullname, username) VALUES ('{id_user}', '{name}', '{username}')"
        )
        self.con.commit()

    def take_id_users(self):
        return self.cur.execute(f"SELECT tg_id FROM tg_users").fetchall()

    def add_user(self, id, id_message, question):
        self.cur.execute(
            f"INSERT INTO send_message (id_name, id_message, question) VALUES ('{id}', '{id_message}', '{question}')"
        )
        self.con.commit()

    def add_in_ls(self, user_id, id_task, id_theory, id_file, section, subsection):
        self.cur.execute(
            f"INSERT INTO ls_tasks (tg_id, id_task, id_theory, id_file, section, subsection) VALUES ('{user_id}', '{id_task}', '{id_theory}', '{id_file}', '{section}', '{subsection}')"
        )
        self.con.commit()

    def take_tg_id_and_question(self, id_message):
        return self.cur.execute(
            f"SELECT id_name, question FROM send_message WHERE id_message = '{id_message}'"
        ).fetchall()[0]

    def add_full_task(self, section, subsection, task_id, theory_id, file_id):
        self.cur.execute(
            f"INSERT INTO tasks (section, subsection, task_id, theory_id, file_id) VALUES ('{section}', '{subsection}', '{task_id}', '{theory_id}', '{file_id}')"
        )
        self.con.commit()

    def take_files_from_ls(self, user_id, section="", subsection=""):
        if section != "":
            files_tuple = self.cur.execute(
                f"SELECT id, id_task, id_theory, id_file, section, subsection FROM ls_tasks WHERE tg_id = '{user_id}' AND section = '{section}'"
            ).fetchall()
            files_list = []
            for i in range(len(files_tuple)):
                files_list.append((files_tuple[i][1], files_tuple[i][2], files_tuple[i][3], files_tuple[i][4], files_tuple[i][5]))
            return files_list
        elif subsection != "":
            files_tuple = self.cur.execute(
                f"SELECT id, id_task, id_theory, id_file, section, subsection FROM ls_tasks WHERE tg_id = '{user_id}' AND subsection = '{subsection}'"
            ).fetchall()
            files_list = []
            for i in range(len(files_tuple)):
                files_list.append((files_tuple[i][1], files_tuple[i][2], files_tuple[i][3], files_tuple[i][4], files_tuple[i][5]))
            return files_list
        else:
            files_tuple = self.cur.execute(
                f"SELECT id, id_task, id_theory, id_file, section, subsection FROM ls_tasks WHERE tg_id = '{user_id}'"
            ).fetchall()
            files_list = []
            for i in range(len(files_tuple)):
                files_list.append((files_tuple[i][1], files_tuple[i][2], files_tuple[i][3], files_tuple[i][4], files_tuple[i][5]))
            return files_list

    def take_from_section(self, tg_id, section):
        files_tuple = self.cur.execute(
            f"SELECT task_id, theory_id, file_id, subsection FROM tasks WHERE section = '{section}'"
        ).fetchall()
        files_list = []
        for i in range(len(files_tuple)):
            your = self.cur.execute(
                f"SELECT id_task FROM ls_tasks WHERE tg_id = '{tg_id}' AND section = '{section}'"
            ).fetchall()
            is_available = False
            for task in your:
                if task[0] == files_tuple[i][0]:
                    is_available = True
                    break
            if not is_available:
                files_list.append(files_tuple[i])
        return files_list

    def take_from_subsection(self, tg_id, subsection):
        files_tuple = self.cur.execute(
            f"SELECT task_id, theory_id, file_id FROM tasks WHERE subsection = '{subsection}'"
        ).fetchall()
        files_list = []
        for i in range(len(files_tuple)):
            your = self.cur.execute(
                f"SELECT id_task FROM ls_tasks WHERE tg_id = '{tg_id}' AND subsection = '{subsection}'"
            ).fetchall()
            is_available = False
            for task in your:
                if task[1] == files_tuple[i][0]:
                    is_available = True
                    break
            if not is_available:
                files_list.append(files_tuple[i])
        return files_list
