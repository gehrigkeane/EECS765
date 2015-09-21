import sys,re

# get input
message = sys.argv[1]

# read in lexicon of words
# download scowl version 7.1
# mk-list english 95 > wordlist
lexicon = set()
roman_only = re.compile('^[A-Z]*$')
for word in open('wordlist').read().upper().split():
  word=word.replace("'",'')
  if roman_only.match(word): lexicon.add(word)

histogram={}
for c in message: histogram[c]=0
for c in message: histogram[c]+=1
frequency_order = map(lambda x:x[1], sorted([(f,c) for c,f in histogram.items()])[::-1])

# returns true if the two maps are compatible.
# they are compatible if the mappings agree wherever they are defined,
# and no two different args map to the same value.
def mergeable_maps(map1, map2):
  agreements = 0
  for c in map1:
    if c in map2:
      if map1[c] != map2[c]: return False
      agreements += 1
  return len(set(map1.values() + map2.values())) == len(map1) + len(map2) - agreements

def merge_maps(map1, map2):
  m = {}
  for (c,d) in map1.items(): m[c]=d
  for (c,d) in map2.items(): m[c]=d
  return m

def search(map, word_maps, outside_lexicon_allowance, words_outside_lexicon):
  cleartext = ''.join(map[x] if x in map else '?' for x in message)
  #print 'trying', cleartext

  # pick a word to try next
  best_word = None
  best_score = 1e9
  for (word,subs) in word_maps.items():
    if word in words_outside_lexicon: continue
    compatible_subs=0
    for sub in subs:
      if mergeable_maps(map, sub): compatible_subs += 1
    unassigned_chars = 0
    for c in word:
      if c not in map: unassigned_chars += 1  #TODO: duplicates?
    if compatible_subs == 0: score = 0
    elif unassigned_chars == 0: score = 1e9
    else: score = 1.0 * compatible_subs / unassigned_chars   # TODO: tweak?
    if score < best_score:
      best_score = score
      best_word = word
  if not best_word:  # no words with unset characters, except possibly the outside lexicon ones
    print cleartext,[''.join(map[x] if x in map else '?' for x in word) for word in words_outside_lexicon]
    return True

  # use all compatible maps for the chosen word
  r = False
  for sub in word_maps[best_word]:
    if not mergeable_maps(map, sub): continue
    r |= search(merge_maps(map, sub), word_maps, outside_lexicon_allowance, words_outside_lexicon)

  # maybe this word is outside our lexicon
  if outside_lexicon_allowance > 0:
    r |= search(map, word_maps, outside_lexicon_allowance - 1, words_outside_lexicon + [best_word])
  return r

for outside_lexicon_allowance in xrange(3):
  # assign the space character first
  for space in frequency_order:
    words = [w for w in message.split(space) if w != '']
    if reduce(lambda x,y:x|y, [len(w)>20 for w in words]): continue  # obviously bad spaces

    # find all valid substitution maps for each word
    word_maps={}
    for word in words:
      n = len(word)
      maps = []
      for c in lexicon:
        if len(c) != n: continue
        m = {}
        ok = 1
        for i in xrange(n):
          if word[i] in m:                      # repeat letter
            if m[word[i]] != c[i]: ok=0; break  # repeat letters map to same thing
          elif c[i] in m.values(): ok=0; break  # different letters map to different things
          else: m[word[i]]=c[i]
        if ok: maps.append(m);
      word_maps[word]=maps

    # look for a solution
    if search({space:' '}, word_maps, outside_lexicon_allowance, []): sys.exit(0)

print 'I give up.'