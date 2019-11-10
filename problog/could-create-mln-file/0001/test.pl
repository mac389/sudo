person(1).
dependent(1,opioids).
use(1,cocaine,_).
evidence(outpatient(1),true).
evidence(adult(1),true).
evidence(male(1),true).
receive(1,buprenorphine_suboxone).
query(detoxification(1,opioid,success)).
query(sample(1,urine,opioids,_,_)).

/*
	Query: What are the chances of successful opioid detoxification? 
	Expected answer: 
	  -- Inpatient, clonidine => 22% (calculated 38)
	  -- Inpatient, suboxone => 77%  (calculated 81.6)
	  -- Outpatient, clonidine => 5%  (calculated 24)
	  -- Outpatient, suboxone 29%.  (calculated 20)
*/