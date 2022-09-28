import re

def find_del_lines(diffs):
  # This function takes a string representing the concatinated diff outputs from
  # a pull request. It returns a list of the deleted lines.

  # Finds all lines of code removed
  if isinstance(diffs, str):
    del_lines = re.findall('^\-$|^\-[^\-].*', diffs, re.MULTILINE)
  else:
    del_lines = []
  # print(f'deleted lines: \n\t{del_lines}\n')

  # Remove leading '-'
  for i in range(len(del_lines)):
    del_lines[i] = del_lines[i][1:]
  
  return del_lines


def find_add_lines(diffs):
  # This function takes a string representing the concatinated diff outputs from
  # a pull request. It returns a list of the files altered and the lines of code
  # in each that was changed. (Files names in the list have a leading '++ ' from
  # the diff. Code changes don't.)

  # Finds all files altered and lines of code altered in each
  if isinstance(diffs, str):
    add_lines = re.findall('^\+$|^\+[^\+].*|^\-\-\-[ ].*', diffs, re.MULTILINE)
  else:
    add_lines = []
  # print(f'added lines: \n\t{add_lines}\n')

  # Remove leading '+'
  for i in range(len(add_lines)):
    add_lines[i] = add_lines[i][1:]
  
  return add_lines


def del_sim(lista, listb):
  # Compares deleted lines represented as two lists
  
  # Find the union of the two sets
  union = list(set(lista) | set(listb))

  # Find the intersection of the two sets
  inter = list(set(lista) & set(listb))

  # print(f'{len(inter)} / {len(union)}') # for debugging
  if len(union) > 0:
    return len(inter)/len(union)
  else:
    return 0 # similarity value for empty changes