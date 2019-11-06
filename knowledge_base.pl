substance = [cocaine,methadone,heroin,alcohol].
therapy = [motivational_enhancement, motivational_interviewing,
standard_intake_evaluation,contingency_management_evaluation, abstinence_based_incentive, residential_treatment,
cognitive_behavioral_therapy].

%Need temporal recourse, need to distinguish between receive and received 

abstinent(X,_) :-
	\+use(X,_). 

woman(X) :-
	person(X),
	female(X).

man(X) :-
	person(X),
	male(X).

adolescent(X) :-
	person(X).
	\+adult(X),
	\+child(X).

smoker(X) :-
	person(X),
	uses(X,nicotine).

pregnant_substance_user(X) :-
	person(X),
	pregnant(X),
	uses(X,Y),
	member(Y,substance).

isSubstance(X) :- 
	%how to look up in list 
	yse.

illicit_drug_user(X) :-
	person(X),
	uses(X,Y),
	member(Y,illicit_drug).

use_stimulant(X) :-
	person(X),
	uses(X,Y),
	member(Y,stimulant).

dependence(X,Y) :-
	%defining for meaning of dependent on substance
	person(X),
	member(Y,substance),
	uses(X,Y). %feels like need more criteria, like the DSM criteria

dependence_on_prescription_opioids(X) :-
	dependence(X,Y),
	member(Y,prescription_opioid).