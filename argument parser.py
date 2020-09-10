import argparse

ap=argparse.ArgumentParser()
ap.add_argument("--n","--name",required=True,help="name of the user")
arg=vars(ap.parse_args())

