#!/usr/bin/python

""" Python module which handles my personal GTD. """

import sys


class GTD:

    def __init__(self, in_filepath, out_filepath):
        done_items = self.process_file(in_filepath)
        self.write_file(out_filepath, done_items)
        print "done items are " + str(len(done_items))

    def process_file(self, in_filepath, keyword='DONE'):
        """ Method to read a file and search for a specific keyword.
        :param str in_filepath: is the file of the path.
        :param str keyword: is the keyword to search inside the file.
        :return dones_list: is a list of the items containing the keyword.
        """
        processed_items = []
        unprocessed_items = []
        # open the file
        with open(in_filepath, 'r') as f:
            # read the file line by line and check if keyword exists
            # in line
            content = f.read().splitlines()
            for line in content:
                if keyword in line:
                    processed_items.append(line)
                else:
                    unprocessed_items.append(line)
        # update the opened file by removing the processed items
        with open(in_filepath, 'w') as f:
            for l in unprocessed_items:
                f.write(l)
                f.write('\n')
        return processed_items

    def write_file(self, out_filepath, contents):
        """ Method to write to update the file with contents.

        :param str out_filepath: is the path of the file to write contents.
        :param list contents: is a list of one string per line.
        """
        with open(out_filepath, 'a') as f:
            # write the contents line by line to the out_filepath
            for line in contents:
                f.write(line)
                f.write('\n')

    def collect_stats(self, processed_item_list, stats_log=''):
        """ Method to collect statistics from items processed.
        If a stats_log file has been given as input, then write the stats
        to a file. Else, just display them.
        :param list processed_item_list: list of processed items
        :param str stats_log: file containing stats.
        """
        # find number of processed items
        num_of_items = len(processed_item_list)

        # if file exists, then write results to a file
        if stats_log:
            # find week number
            today = datetime.today()
            week = today.strftime("%U")
            weeknum = "W"+str(week)
            # create entry
            entry = weeknum + "," + str(num_of_items)
            with open(stats_log, 'a') as f:
                f.write(entry)
                f.write("\n")
        else:
            print "number of items processed: " + str(num_of_items)
