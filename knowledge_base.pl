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
therapy(behavioral_strategic_family_therapy).
therapy(hiv_ed).

prescription_opioid(percocet).
prescription_opioid(fentanyl).
prescription_opioid(oxycodone).


opioid(oxycodone).
opioid(fentanyl).
opioid(morphine).
opioid(heroin).
opioid(percocet).
%opioid(methadone).

risky_behavior(drug_use).

illicit_drug(heroin).
illicit_drug(fentanyl).

stimulant(cocaine).
stimulant(amphetamine).

sex(male).
sex(female).

P::property(X,location,inpatient);(1-P)::property(X,location, outpatient) :- 
	inpatient(X),
	P is 1. 

P::property(X,location,outpatient);(1-P)::property(X,location, inpatient) :- 
	outpatient(X),
	P is 1. 

P::inpatient(X);(1-P)::outpatient(X) :- 
	property(X,location,inpatient),
	P is 1.

P::outpatient(X);(1-P)::inpatient(X) :-
	property(X,location,outpatient),
	P is 1. 

property(X,use,Y) :- property(X,dependence,Y).

property(X,dependence,opioids) :-
	property(X,dependence,Y),
	opioid(Y).

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

0.1::inject(X,Y,T) :-  %DITTO
	use(X,Y),
	member(Y,[cocaine,heroin,amphetamine,fentanyl]).

sample(X,Y,positive,Z) :- \+sample(X,Y,negative,Z).

0.1::pregnant(X) :- gender(X,female).


/* From CTN-0009. 
   Representation of: Nicotine dependence is highly prevalent 
   among drug- and alcohol-dependent patients. 

   I use 80% to operationalize "highly prevalent"
*/

P::property(X,use,nicotine) :- 
   property(X,use,Z),
   substance(Z), %I have defined alcohol as a substance
   P is 0.8.

/* From CTN-0010
	Representation of: The usual treatment for opioid-addicted youth 
	is detoxification and counseling. 

*/

P::receive(X,detoxification);P::receive(X,counseling) :-
	property(X,age,youth),
	property(X,dependence,opioids),
	P is 1.

receive(X,detoxification) :-
	receive(X,buprenorphine);
	receive(X,buprenorphine_naloxone).

inpatient :- \+outpatient.

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

use_illicit_drugs(X) :-
	use(X,Y,_),
	illicit_drug(Y).

use_stimulant(X) :-
	use(X,Y,_),
	stimulant(Y).