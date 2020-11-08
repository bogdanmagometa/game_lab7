"""
This module contains function and some stuff related to printing text to
terminal in a nice way.

Contents:
1) ASCII_UCU_LOGO - string with UCU logo
2) indent_print(text, indent, time_per_letter, prior_text) - function that can
print text letter by letter and with indent.
"""

import time


ASCII_UCU_LOGO = """                                   ..                                 
                                 .......                              
                        ....       ..       ....                      
                   ..        ..           .        ..                 
               ...      ..   .    ....    .   ..      ...             
       ..                         ....                         ..     
       .. ..                      ....          .            . ..     
       .. ..      .....           ....     ...     ..        . ..     
       .. ..        .....         ....   ..       ..         . ..     
       .. ..         .....        .... ..                    . ..     
       .. ..          .....       ......                     . ..     
       .. ..            .....     .........            ...   . ..     
       .. ..             .....   .....  .....         ...    . ..     
       .. ..               ...........   .....       ..      . ..     
       .. ..                 ...  ....    .....    ...       . ..     
       .. ..               ...    ....      ........         . ..     
       .. ..             ...      ....         ...           . ..     
       .. ..            ..        ....       ...             . ..     
       .. ..         ...          ....     ...               . ..     
       .. ..      ..              ...    ...                 . ..     
       .. ..                   ..      ...                   . ..     
       .. ..                   ..    ...                     . ..     
          ..   ............                  ............    .        
                               ..      ..                             
                                   ..                                """

def indent_print(text: str, indent: int, time_per_letter: float,
                                                        prior_text="") -> None:
    """
    Prints text letter by letter.

    Parameter indent is number of lines that will be between the line where
    text begins and lower bound of the terminal.

    time_per_letter - is the time in seconds for printing single letter.
    prior_text - is the text printed without delay before printing text.
    """
    # Don't try to understand the code. I don't understand it myself.

    cur_text = prior_text
    num_lines_in_prior = prior_text.count('\n')

    num_line = 0
    for line in text.split('\n'):

        if num_line != 0:
            cur_text += "\n"

        for letter in line:
            print('\n'*30)
            cur_text += letter
            print(cur_text, end="")

            print('\n'*(indent-num_line-num_lines_in_prior), end="", flush=True)

            time.sleep(time_per_letter)

        print('\n'*100)
        print(cur_text, end="")
        print('\n'*(indent-num_line-num_lines_in_prior), end="", flush=True)

        num_line += 1
