

flight(toronto,aircanada,london,550,420).
flight(toronto,united,london,700,480).
flight(toronto,united,madrid,1000,600).
flight(toronto,ibeira,madrid,850,540).
flight(toronto,aircanada,madrid,950,540).

flight(london,aircanada,toronto,575,440).
flight(london,united,toronto,725,500).
flight(london,ibeira,barcelona,295,320).

flight(barcelona,ibeira,london,260,270).
flight(barcelona,ibeira, valencia,150,105).
flight(barcelona,ibeira, madrid,160,95).
flight(barcelona,aircanada,madrid,140,90).

flight(madrid, aircanada, barcelona, 175, 105).
flight(madrid, ibeira, barcelona, 205, 110).
flight(madrid, ibeira, valencia, 115, 95).
flight(madrid, ibeira, malaga, 125, 105).
flight(madrid, ibeira, toronto, 875, 525).
flight(madrid, united, toronto, 1025, 585).
flight(madrid, aircanada, toronto, 975, 525).

flight(valencia, ibeira, barcelona, 150, 95).
flight(valencia, ibeira, madrid, 80, 70).
flight(valencia, ibeira, malaga, 120, 140).

flight(malaga, ibeira, valencia, 130, 150).
flight(malaga, ibeira, madrid, 100, 90).

flight(paris, united, toulouse, 85,  180).

flight(toulouse, united, paris, 75, 150).

airport(toronto, 50, 60).
airport(barcelona, 40, 30).
airport(madrid, 75, 45).
airport(valencia, 40, 20).
airport(malaga, 50, 30).
airport(paris, 50, 60).
airport(toulouse, 40, 30).
airport(london, 75, 80).



is_flight_from_x_to_y(X, Y) :- flight(X, _, Y, _, _). 

is_cheap(A, C, B):-flight(A, C, B, P, _), P < 400.    

is_possible_from_x_to_y_intwo_flight(A, B):-flight(A, _,Z, _, _),flight(Z, _, B, _, _), Z \== A, Z \== B. 

is_cheap_is_aircanada(A, C, B):-flight(A, C, B, P, _), P < 400; C == aircanada. 

is_notunited_is_aircanada(A, B):-flight(A, C, B, _, _), C \== united.

is_united_is_aircanada(A, B):-flight(A, C, B, _, _), C == united -> flight(A, D, B, _, _), D==aircanada.


                                                                                                                                                                                    










