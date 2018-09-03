#coding=utf-8

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

        parser.add_argument('--namespace',
                            required=False,
                            action='store',
                            help="Namespace")

        args = parser.parse_args()

        return args

    args = get_args()

    k8s = Connection(args.server,args.token)
    k8s.setConnection()
#    k8s.setNamespace(args.namespace)
    k8s.listPodsForAllNamespaces()
#    k8s.listNamespacedPods(args.namespace)
    k8s.listStorageClass()
