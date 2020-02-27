from xml.etree import ElementTree as ET
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--print', action='store_true', help='prints resulting xml output to console')
parser.add_argument('--sort', action='store', nargs=1, metavar='N', help='randomly sorts data into N groups')
parser.add_argument('filename', nargs=1, action='store', help='name of xml file to be opened')
args = parser.parse_args()
xml_file = args.filename[0]
tree = ET.parse(xml_file)
root = tree.getroot()

