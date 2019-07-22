from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable


p = PrologString("""

P::urine(X,opioid_free,initial);(1-P)::urine(X,contains_opioids, initial) :-
    P is 0.5.

P::urine(X,opioid_free,n1_month);(1-P)::urine(X,contains_opioids,n1_month) :-
	taper(X,buprenorphine,n28_days),
	P is 0.18.

P::urine(X,opioid_free,n3_month);(1-P)::urine(X,contains_opioids,n3_month) :-
	taper(X,buprenorphine,n28_days),
	P is 0.18.

P::urine(X,opioid_free,n1_month);(1-P)::urine(X,contains_opioids,n1_month) :-
	taper(X,buprenorphine,n7_days),
	P is 0.12.

P::urine(X,opioid_free,n3_month);(1-P)::urine(X,contains_opioids,n3_month) :-
	taper(X,buprenorphine,n7_days),
	P is 0.13.

P::urine(X,opioid_free, initial);(1-P)::urine(X,contains_opioids,initial) :-
	taper(X,buprenorphine,n28_days),
	P is 0.30.

P::urine(X,opioid_free, initial);(1-P)::urine(X,contains_opioids,initial) :-
	taper(X,buprenorphine,n7_days),
	P is 0.44.
	
person(1).
taper(1,buprenorphine,n7_days).
query(urine(1,_,_)).
""")

print get_evaluatable().create_from(p).evaluate()