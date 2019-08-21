#! /usr/bin/env Python3

import argparse

from datetime import datetime
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker

from db.tabledef import Entry


db_engine = create_engine('sqlite:///blog.sqlite3')

class MicroBlog:
    def __init__(self):
        self.db_session = sessionmaker(bind=db_engine)
        self.session = self.db_session()

    def submit_entry(self, content):
        try:
            timestamp = datetime.now()
            entry = Entry(timestamp, content)

            self.session.add(entry)
            self.session.commit()

            print('[*] Entry has been submitted.')

        except Exception as ex:
            print('[*] Error -> ' + str(ex))

        finally:
            print('[*] Closing')
            self.session.close()


if __name__ == '__main__':
    micro_blog = MicroBlog()
    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--message', type=str)

    args = parser.parse_args()
    micro_blog.submit_entry(args.message)


