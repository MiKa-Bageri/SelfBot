import aiosqlite


class DBController:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path

    async def handle_user(self, user_id: int):
        async with aiosqlite.connect(self.db_path) as db:

            cursor = await db.execute(
                "SELECT * FROM users WHERE user_id = ?",
                (user_id,)
            )

            is_exist = await cursor.fetchone()

            if is_exist is None:
                await db.execute(
                    "INSERT INTO users VALUES (?, ?, ?)",
                    (user_id, 0, 0)
                )

                await db.commit()
                return True

            return False

    async def handle_test(self, user_id: int):
        async with aiosqlite.connect(self.db_path) as db:

            cursor = await db.execute(
                "SELECT is_test FROM users WHERE user_id = ?",
                (user_id,)
            )

            is_first_time = await cursor.fetchone()

            if is_first_time and is_first_time[0] == 0:

                await db.execute(
                    "UPDATE users SET is_test = 1 WHERE user_id = ?",
                    (user_id,)
                )

                await db.commit()
                return True

            return False

    async def add_customer(self, user_id: int):
        async with aiosqlite.connect(self.db_path) as db:

            await db.execute(
                "UPDATE users SET is_customer = 1 WHERE user_id = ?",
                (user_id,)
            )

            await db.commit()

    async def get_customers(self):
        async with aiosqlite.connect(self.db_path) as db:

            cursor = await db.execute(
                "SELECT user_id FROM users WHERE is_customer = 1"
            )

            return await cursor.fetchall()