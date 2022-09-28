def check_path_sim(fpaths1, fpaths2):
  # Split strings into individual file paths stored as list of strings
  files1 = fpaths1.split(',')
  files2 = fpaths2.split(',')

  # Initialize list to store pairwise tuples of file path similarity
  similarities = []

  # Loop through all pairs of files
  for f1 in files1:
      for f2 in files2:
        # Inserts the tuples (f1, f2, their similarity %) into similarities
        similarities.append( (f1, f2, check_path_sim_pair(f1, f2)) )
  
  # Sort the list by similarity values (high to low)
  similarities.sort(key = lambda x: x[2], reverse=True)

  # Find k top similarity values, where k is the length of the shorter file list
  k = min(len(files1), len(files2))
  top_k = []

  while k > 0:
    top_sim = similarities.pop(0)
    top_k.append(top_sim[2])
    
    # Delete other entries in similarities which share files with top_sim (thus
    # avoiding counting close similarity to any single file twice)
    for sim in similarities:
      if sim[0] == top_sim[0] or sim[1] == top_sim[1]:
        similarities.remove(sim)

    k -= 1

  # Return the sum of the top similarity values divided by the length of the longer files list
  return sum(top_k) / max(len(files1), len(files2))

def check_path_sim_pair(fpath1, fpath2):
  # Split strings into path components ("bits") stored as list of strings
  path_bits1 = fpath1.split('/')
  path_bits2 = fpath2.split('/')
  mx_len = max(len(path_bits1), len(path_bits2)) # Save number of bits in longer string

  # Now loop through the bits as long as they match
  len_match = 0 # Variable to store number of matching bits in the two path strings
  while len(path_bits1) > 0 and len(path_bits2) > 0:
    if path_bits1.pop(0) == path_bits2.pop(0):
      len_match += 1
    else:
      break
  
  # Now convert the number of matching elements into a percentage match (range 0-1)
  return len_match / mx_len