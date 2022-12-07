module smart_toilet (
    soln1,
    soln2,
    soln3,
    out
);

input   soln1, soln2, soln3, soln4, soln5, soln6;
output  out;

// connect0,  

wire    connect1,  connect2,  connect3,  connect4,  connect5,  connect6,  connect7, connect8, connect9, connect10, connect11, connect12, connect13, connect14, connect15, connect16;
//,  connect8,  connect9,
//        connect10, connect11, connect12;

//F Prime
serpentine_150px_0   serp0   (.in_fluid(soln1), .out_fluid(connect0));

//R Prime
serpentine_150px_0   serp1   (.in_fluid(soln2), .out_fluid(connect1));


//serpentine_100px_0  serp2   (.in_fluid(connect1), .out_fluid(connect2));

// diffmix_25px_0      mix0    (.a_fluid(soln1), .b_fluid(connect2), .out_fluid(connect3));
diffmix_25px_0      mix0    (.a_fluid(connect0), .b_fluid(connect1), .out_fluid(connect2));

//Evagreen
serpentine_25px_0   serp2   (.in_fluid(soln3), .out_fluid(connect3));
serpentine_50px_0   serp3   (.in_fluid(connect3), .out_fluid(connect4));
serpentine_150px_0   serp4   (.in_fluid(connect4), .out_fluid(connect5));

diffmix_25px_0      mix0    (.a_fluid(connect5), .b_fluid(connect2), .out_fluid(connect6));

//H2O

serpentine_50px_0   serp1   (.in_fluid(soln4), .out_fluid(connect7));
serpentine_150px_0   serp1   (.in_fluid(connect7), .out_fluid(connect8));

diffmix_25px_0      mix0    (.a_fluid(connect8), .b_fluid(connect6), .out_fluid(connect9));

// Taq
serpentine_75px_0  serp3   (.in_fluid(soln5), .out_fluid(connect10));
serpentine_200px_0  serp4   (.in_fluid(connect10), .out_fluid(connect11));

diffmix_25px_0      mix0    (.a_fluid(connect11), .b_fluid(connect9), .out_fluid(connect12));


// DNA
serpentine_150px_0   serp1   (.in_fluid(soln6), .out_fluid(connect13));
serpentine_200px_0   serp1   (.in_fluid(connect13), .out_fluid(connect14));
serpentine_50px_0   serp1   (.in_fluid(connect14), .out_fluid(connect15));

diffmix_25px_0      mix0    (.a_fluid(connect15), .b_fluid(connect12), .out_fluid(connect16));



//serpentine_300px_0  serp6   (.in_fluid(connect6), .out_fluid(connect8));
// serpentine_300px_0  serp7   (.in_fluid(connect8), .out_fluid(connect9));
// serpentine_300px_0  serp8   (.in_fluid(connect9), .out_fluid(connect10));
// serpentine_300px_0  serp9   (.in_fluid(connect10), .out_fluid(connect11));
// serpentine_300px_0  serp10  (.in_fluid(connect11), .out_fluid(connect12));

//diffmix_25px_0      mix1    (.a_fluid(connect3), .b_fluid(connect6), .out_fluid(connect7));

serpentine_300px_0  serp11  (.in_fluid(connect16), .out_fluid(out));

endmodule