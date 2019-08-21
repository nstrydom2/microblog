#! /usr/bin/env python3

import argparse

from datetime import datetime
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker

from db.tabledef import Entry


db_engine = create_engine('sqlite:////home/ghost/PycharmProjects/microblog/blog.sqlite3')

class MicroBlog:
    def __init__(self):
        self.db_session = sessionmaker(bind=db_engine)
        self.session = self.db_session()

    def print_last_entries(self, num_entries):
        try:
            results = \
                self.session.query(Entry.timestamp, Entry.content).order_by(Entry.timestamp.desc()).limit(num_entries)

            print('[*] Printing {} results'.format(results.count()))

            for row in results:
                print('[*] {:.19} -- {}'.format(str(row[0]), row[1]))

        except Exception as ex:
            print('[*] Error -> ' + str(ex))

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

    parser.add_argument('-m', '--message', type=str, help='message to submit to microblog')
    parser.add_argument('-p', '--print', type=int, default=10, required=False, help='prints last n entries')

    args = parser.parse_args()

    if args.message is not None:
        micro_blog.submit_entry(args.message)
    elif args.print is not None or args.print > 0:
        micro_blog.print_last_entries(args.print)


