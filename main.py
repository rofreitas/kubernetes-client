# coding=utf-8
#!C:\Python27\python.exe

from k8s import Connection

import argparse

class Main():
    def get_args():
        parser = argparse.ArgumentParser()

        parser.add_argument('--server',
                            required=True,
                            action='store',
                            help='Server Address')

        parser.add_argument('--token',
                            required=True,
                            action='store',
                            help="ApiToken")

        args = parser.parse_args()

        return args

    args = get_args()

    k8s = Connection(args.server,args.token)
    k8s.openConnection()
    k8s.k8Api()
    k8s.getPods()
