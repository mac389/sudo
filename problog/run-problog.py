from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable


p = PrologString("""

2*P::stay_in_therapy(X, n28_day);(1-2*P)::not_stay_in_therapy(X,n_28_day) :-
    receive_initial_therapy(X,motivational_interviewing),
    P is 0.33.

P:urine_drug_screen(X, positive);(1-P)::urine_drug_screen(X, negative) :-
    receive_initial_therapy(X,motiavtional_interviewing),
    P is 0.5.

P::stay_in_therapy(X, n84_day);(1-P)::not_stay_in_therapy(X,n84_day) :-
    receive_initial_therapy(X,standard_intake_evaluation),
    P is 0.5.
    
P::urine_drug_screen(X, positive);(1-P)::urine_drug_screen(X, negative) :-
    receive_initial_therapy(X,standard_intake_evaluation),
    P is 0.5.


	
person(1).
receive_initial_therapy(1,standard_intake_evaluation).
query(stay_in_therapy(1,n84_day)).
""")

print get_evaluatable().create_from(p).evaluate()