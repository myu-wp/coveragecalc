import argparse
from . import coveragecalc


def main():
    parser = argparse.ArgumentParser(description='Outputs IDC coverage from a given csv.')
    parser.add_argument('infile', help='input xlsx/csv that contains Identity Check API output cols')
    parser.add_argument('-o', '--outfile', default='output.xlsx',
                        help='output excel file name (default: %(default)s)')
    args = parser.parse_args()

    coveragecalc.main(args)