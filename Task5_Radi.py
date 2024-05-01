from Task2_Radi import *
from Task2_Radi import lst
from Task3_Radi import *
from Task3_Radi import subbrute as t3_sub
from Task3_Radi import crawl as t3_crawl
from Task3_Radi import screenshot as t3_screen
from Task4_Radi import *
import json,requests
import argparse

parser = argparse.ArgumentParser(description='Scan domains actively or passively.')
parser.add_argument('--scan_type', type=str, choices=['passive','active','cloud'], help='cloud will perform brute force on cloud storage accounts')
parser.add_argument('--domain', type=str, help='Domain to scan')
args = parser.parse_args()

if args.scan_type == 'passive':
        if not args.domain:
            parser.error("For pasive Scan, you need to provide domain using --domain")
        Passive =Passivebase(args.domain)

elif args.scan_type == 'active':
        if not args.domain:
            parser.error("For active Scan, you need to provide domain using --domain")
        Active = Activebase(args.domain)
elif args.scan_type == 'cloud':
        if not args.domain:
            parser.error("For cloud Scan, you need to provide domain using --domain")
        cloud = Cloudbase(args.domain)
else:
        parser.error("Invalid scan type. Please choose either 0 for Active Scan or 1 for Passive Scan.")
