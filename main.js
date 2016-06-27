/**
 * Created by Trinity on 27/06/2016.
 * Author: Julio Manso
 */
"use strict";

import Call from "./Call.js";

process.on("uncaughtException", function (err) {
    console.error(err.toString());
});


const RADIUS = process.argv[2] || 100;
const PATH = process.argv[3] || "./customer.json";
const LAT = process.argv[4] || 53.3381985;
const LON = process.argv[5] || -6.2592576;

let call = new call(RADIUS, LAT, LON, PATH);
call.display();