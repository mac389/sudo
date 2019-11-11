substance(cocaine).
substance(methadone).
substance(heroin).
substance(alcohol). 
substance(amphetamine).
substance(nicotine).

therapy(motivational_enhancement).
therapy(motivational_interviewing).
therapy(motivational_incentives).
therapy(computer_modules).
therapy(care_as_usual).
therapy(standard_care).
therapy(outpatient_addiction_treatment).
therapy(standard_intake_evaluation).
therapy(contingency_management_evaluation).
therapy(abstinence_based_incentive).
therapy(residential_treatment).
therapy(cognitive_behavioral_therapy).
therapy(safer_skills_building).
therapy(hiv_ed).

prescription_opioid(percocet).
prescription_opioid(fentanyl).
prescription_opioid(oxycodone).

risky_behavior(drug_use).

illicit_drug(heroin).
illicit_drug(fentanyl).

stimulant(cocaine).
stimulant(amphetamine).

sex(male).
sex(female).

taper(_,_,_).

adolescent(_).

success :- \+failure.
positive :- \+negative.
in_treatment :- in_therapy.

n4_weeks :- n1_month.
n12_weeks :- n3_month.

standard_care :-
	care_as_usual;
	counseling_as_usual.

receive(X,buprenorphine) :-
	receive(X,buprenorphine_naloxone).

0.9::outpatient(X). %fit to parameters, need to cite sources
0.1::inject(X,Y,T) :-  %DITTO
	use(X,Y),
	member(Y,[cocaine,heroin,amphetamine,fentanyl]).

sample(X,Y,positive,Z) :- \+sample(X,Y,negative,Z).

0.1::pregnant(X) :- gender(X,female).

inpatient(X) :- \+outpatient(X).

gender(X,Y) :-
	person(X),
	sex(Y).

smoker(X) :-
	person(X),
	use(X,nicotine,_).

pregnant_substance_user(X) :-
	use(X,Y,_),
	pregnant(X),
	substance(Y).

illicit_drug_user(X) :-
	use(X,Y,_),
	illicit_drug(Y).

use_stimulant(X) :-
	use(X,Y,_),
	stimulant(Y).

use(X,Y,_) :-
	dependent(X,Y).

use(X,Y,_) :- use(X,Y).

use(X,Y) :- dependent(X,Y).

0.05::use(X,Y,before) :- %background probability
	person(X,_),
	substance(Y).

dependent_on_prescription_opioids(X) :-
	dependent(X,Y,_),
	prescription_opioid(Y).