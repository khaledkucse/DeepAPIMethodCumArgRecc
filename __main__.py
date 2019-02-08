import config
from pathlib import Path
from DataPreprocessing import Vocab,Lang
from TFEstimatorOperation import TFTraining,TFOneTesting,TFTesting
from KerasOperation import Training,Testing,OneTesting


config.init()

input_vocab_size = config.MAX_VOCAB_SIZE_INPUT+ 3
output_vocab_size = config.MAX_VOCAB_SIZE_OUTPUT+ 3

input_lang = Lang()
output_lang = Lang()

var = input("Enter one of the mode: \n"
            " train : To train the model \n"
            " test: To test the model \n"
            " train-test: To train and then test \n"
            " infer: To see result for a single instance \n")

if var == 'train':

    #Keras Seq2Seq Implementation
    if config.which_implementation == 'keras':
        training = Training(input_vocab_size = input_vocab_size,
                            output_vocab_size = output_vocab_size)

    # Tensorflow Seq2Seq Implementation
    elif config.which_implementation == 'tf':
        training = TFTraining(input_vocab_size=input_vocab_size,
                              output_vocab_size=output_vocab_size)

    # Tensorflow Estimator Seq2Seq Implementation
    elif config.which_implementation == 'tf_estimator':
        training = TFTraining(input_vocab_size = input_vocab_size,
                              output_vocab_size = output_vocab_size)

    vocab_check = input("Are you going to Save the damca_vocabulary(y/n): ")

    if 'y' in vocab_check:
        training.train(is_save_vocabulary=True)

    else:
        training.train(is_save_vocabulary=False)


elif var == 'test':

    print('Loading Input Vocabulary.....')
    input_lang = Vocab.load_vocabulary(Vocab,
                                       datapath = config.input_vocab_file_path,
                                       langName = 'Context',
                                       max_size = input_vocab_size)
    print('Loading Output Vocabulary....')
    output_lang = Vocab.load_vocabulary(Vocab,
                                        datapath = config.output_vocab_file_path,
                                        langName = 'Label',
                                        max_size = output_vocab_size)

    # Keras Seq2Seq Implementation
    if config.which_implementation == 'keras':
        model_file = Path(config.model_file_path)
        if model_file.is_file():
            testing = Testing(input_vocab_size=input_vocab_size,
                              output_vocab_size=output_vocab_size,
                              input_lang=input_lang,
                              output_lang=output_lang)

    # Tensorflow Seq2Seq Implementation
    if config.which_implementation == 'tf':
        testing = TFTesting(input_vocab_size=input_vocab_size,
                            output_vocab_size=output_vocab_size,
                            input_lang=input_lang,
                            output_lang=output_lang)


    # Tensorflow Estimator Seq2Seq Implementation
    if config.which_implementation == 'tf_estimator':
        print("Implementing Tensorflow Estimator Version.....")
        testing = TFTesting(input_vocab_size = input_vocab_size,
                            output_vocab_size = output_vocab_size,
                            input_lang = input_lang,
                            output_lang = output_lang)
    testing.test()


elif var == 'infer':
    print('Loading Input Vocabulary.....')
    input_lang = Vocab.load_vocabulary(Vocab,
                                       datapath = config.input_vocab_file_path,
                                       langName = 'Context',
                                       max_size = input_vocab_size)
    print('Loading Output Vocabulary....')
    output_lang = Vocab.load_vocabulary(Vocab,
                                        datapath = config.output_vocab_file_path,
                                        langName = 'Label',
                                        max_size = output_vocab_size)

    # Keras Seq2Seq Implementation
    if config.which_implementation == 'keras':
        model_file = Path(config.model_file_path)
        if model_file.is_file():
            seq_input = input("Please enter the input in the following format \n"
                          " ID +++$+++ <label Sequence> +++$+++ <reciever type> +++$+++ <context sequence> \n")
            testing = OneTesting(input_vocab_size=input_vocab_size,
                                output_vocab_size=output_vocab_size,
                                input_lang=input_lang,
                                output_lang=output_lang,
                                input_seq=seq_input)


    #Tensorflow Seq2seq Implementation
    if config.which_implementation == 'tf':
        seq_input = input("Please enter the input in the following format \n"
                          " ID +++$+++ <label Sequence> +++$+++ <reciever type> +++$+++ <context sequence> \n")

        testing = TFOneTesting(input_vocab_size=input_vocab_size,
                                output_vocab_size=output_vocab_size,
                                input_lang=input_lang,
                                output_lang=output_lang,
                                input_seq=seq_input)

    # Tensorflow Estimator Seq2seq Implementation
    if config.which_implementation == 'tf_estimator':
        seq_input = input("Please enter the input in the following format \n"
                              " ID +++$+++ <label Sequence> +++$+++ <reciever type> +++$+++ <context sequence> \n")

        testing = TFOneTesting(input_vocab_size=input_vocab_size,
                                output_vocab_size=output_vocab_size,
                                input_lang=input_lang,
                                output_lang=output_lang,
                                input_seq=seq_input)


    testing.test()






