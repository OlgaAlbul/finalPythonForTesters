import argparse


def main():
    parser = argparse.ArgumentParser(description='���������� ����� � ������ � ��������������� �������.')
    parser.add_argument('number', type=int, help='����� ��� ������')
    parser.add_argument('text', type=str, help='������ ��� ������')
    parser.add_argument('--verbose', action='store_true',
                        help='����� �������������� ����������')
    parser.add_argument('--repeat', type=int, default=1,
                        help='���������� ���������� ������')
    args = parser.parse_args()
    if args.verbose:
        print(f'���������� ���������: number={args.number},text = "{args.text}", repeat = {args.repeat}')
        print(f'�����: {args.number}, ������: {args.text * args.repeat}')


if __name__ == '__main__':
    main()
