import argparse
import my_multiprocessing
import Simple_DNNClassifier_tensorflow

parser = argparse.ArgumentParser(description='Execute Python Demo programs')
parser.add_argument('--program',
                    help='''
                        multiprocessing - Multiprocessing program with shared objects and values
                        dnn_tensorflow  - Simple DNN classifier example using inbuilt one''')


if __name__ == "__main__":
    args = parser.parse_args()
    programs = {
        "multiprocessing": my_multiprocessing,
        "dnn_tensorflow": Simple_DNNClassifier_tensorflow
    }
    if args.program in programs.keys():
        print(args.program, "program is started")
        programs[args.program].run()
    else:
        parser.print_help()