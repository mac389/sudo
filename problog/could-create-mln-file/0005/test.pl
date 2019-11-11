person(1,male).
dependent(1,opioids).
use(1,cocaine,before).
receive(1,buprenorphine_naloxone).
receive(1,motivational_enhancement).
receive(1,standard_care).
hispanic(1).
taper(1,buprenorphine,n7_days).

evidence(outpatient(1),true).
evidence(hispanic(1),true).

query(detoxification(1,opioid,success)).
query(remain(X,in_therapy,_)).
query(use(1,_,_)).
query(taper(1,_,_)).
query(sample(1,urine,opioids,_,_)).