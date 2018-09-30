import os, json, math, random

from pprint import pprint 

n_patients = 3 

axioms = [x.strip() for x in open('1005.predicates','r').read().splitlines() if x]
n_axioms_per_patient = int(math.floor(0.6*len(axioms)))
db = []

for i in xrange(n_patients):
	tmp = [random.sample(axioms,n_axioms_per_patient)]
	#Assume default argument is "person" in all predicates. 
	#I should eventually remove this harcoded solution.
	tmp = [axiom.replace('person','')]
	pprint(tmp)


'''
illicit_drug_user(person)
newly_infected_with_HCV(person)
evaluated_for_HCV(person)
racial_minority(person)
ethnic_minority(person)
chronically_infected_with_HCV(person)
die_from_HCV(person)

//Converted to CNF
log(0.8) !newly_infected_with_HCV(x) v illicit_drug_user(x)

//Original form
// (newly_infected_with_HCV(x) ^ evaluated_for_HCV(x)) => illicit_drug_user(x)
log(0.8) !newly_infected_with_HCV(x) v evaluated_for_HCV(x) v illicit_drug_user(x) 

log(0.8) !newly_infected_with_HCV(x) v racial_minority(x)
log(0.8) !chronically_infected_with_HCV(x) v racial_minority(x)

log(0.8) !die_from_HCV(x) v racial_minority(x)
log(0.8) !newly_infected_with_HCV(x) v ethnic_minority(x)

log(0.8) !chronically_infected_with_HCV(x) v ethnic_minority(x)
log(0.8) !die_from_HCV(x) v ethnic_minority(x)

/*
//Findings
log(0.8) (tested_for_HCV(x) ^ illicit_drug_user(x)) => tested_for_HCV_where_receiving_drug_abuse_treatment(x)
log(0.8) (!tested_for_HCV(x) ^ illicit_drug_user(x)) => unaware_of_voluntary_test_sites(x)
log(0.8) (tested_positive_for_HCV(x) ^ unsure_of_meaning_of_testing_positive_for_HCV(x)) => illicit_drug_user(x)
log(0.8) illicit_drug_user(x) => (mistrust_healthcare_provider_motivations(x) ^ do_not_pursue_HCV_treatment(x))
log(0.8) illicit_drug_user(x) => source_of_information_about_HCV(social_networks)
log(0.8) illicit_drug_user(x) => soutce_of_information_about_HCV(social_ineractions)
*/
'''