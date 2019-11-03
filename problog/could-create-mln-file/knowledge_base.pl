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

pregnant_substance_user(X) :-
	person(X),
	pregnant(X),
	uses(X,Y),
	isSubstance(Y).

isSubstance(X) :- 
	%how to look up in list 
	yse.

illicit_drug_user(X) :-
	person(X),
	uses(X,Y),
	isIllicitDrug(Y).

use_stimulant(X) :-
	person(X),
	uses(X,Y),
	isStimulant(Y).

dependence(X,Y) :-
	%defining for meaning of dependent on substance
	person(X),
	isSubstance(Y),
	uses(X,Y). %feels like need more criteria, like the DSM criteria

dependence_on_prescription_opioids(X) :-
	dependence(X,Y),
	isPrescriptionOpioid(Y).