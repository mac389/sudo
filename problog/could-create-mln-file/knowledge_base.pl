substance = [cocaine,methadone,heroin,alcohol].

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