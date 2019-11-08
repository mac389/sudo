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


success :- \+failure.
positive :- \+negative.
in_treatment :- in_therapy.

0.9::outpatient(X). %fit to parameters, need to cie sources
0.4::use(_,cocaine). %now add for other drugs
0.5::adult(X). %CITATION NEEDED
0.5::male(X). %DITTO
0.5::female(X). %DITTO
0.4::hispanic(X). %DITTO

0.1::inject(X,Y) :-  %DITTO
	use(X,Y),
	member(Y,[cocaine,heroin,amphetamine,fentanyl]).

sample(X,Y,Z,positive) :- \+sample(X,Y,Z,negative).

youth(X) :- \+adult(X).

0.1::pregnant(X) :- female(X).
female(X) :- \+male(X).

inpatient(X) :- \+outpatient(X).

use(X,Y) :- 
    person(X),
    substance(Y).
    
therapy(X) :-
	treatment(X).

abstinent(X,_) :-
	\+use(X,_). 

woman(X) :-
	person(X),
	female(X).

man(X) :-
	person(X),
	male(X).

adolescent(X) :-
	\+adult(X).

female(X) :- 
	\+male(X).

smoker(X) :-
	person(X),
	uses(X,nicotine).

pregnant_substance_user(X) :-
	person(X),
	pregnant(X),
	use(X,Y),
	substance(Y).

illicit_drug_user(X) :-
	person(X),
	use(X,Y),
	illicit_drug(Y).

use_stimulant(X) :-
	person(X),
	use(X,Y),
	stimulant(Y).

dependent(X,Y) :-
	%defining for meaning of dependent on substance
	%feels like need more criteria, like the DSM criteria
	person(X),
	substance(Y),
	use(X,Y). 

dependent_on_prescription_opioids(X) :-
	dependent(X,Y),
	prescription_opioid(Y).