from paillier.paillier import *
import random; import copy


#Global publci key
alice_pub = 0;
alice_priv, local_pub = generate_keypair(128)

#ini_states = (re.sub('[{} ]', '', raw_input("\n").split(':')[1])).strip().split(',')

print str(local_pub)
def Alice():
	
	#alice_pub = copy.deepcopy(local_pub)
	#k = encrypt(local_pub, 2)
	#print k

	Bob(10)

def Bob(how_many_inputs_alice):
	gather_user_input(how_many_inputs_alice)

def gather_user_input(how_many_inputs_alice):
	inputs = []
	x = encrypt(local_pub, 2)
	print x
	# for x in range(how_many_inputs_alice):
	# 	inpt = random.randint(1, 10000)
	# 	#k = encrypt(alice_pub, 2)
	# 	#print k

	#inputs = [encrypt(alice_pub, random.randint(1, 10000)) for x in range(how_many_inputs_alice)]
	print inputs

Alice()