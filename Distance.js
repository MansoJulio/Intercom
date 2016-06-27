/**
 * Created by Trinity on 27/06/2016.
 */
"use strict";


const EARTH_RADIUS = 6378.137;

/**
 * Return the distance between Point A and Point B in km
 * @param {Number} latA : Latitude of Point A in degree
 * @param {Number} lonA : Longitude of Point A in degree
 * @param {Number} latB : Latitude of Point B in degree
 * @param {Number} lonB : Longitude of Point B in degree
 */
export default function getCircleDistance(latA, lonA, latB, lonB) {
    latA *= Math.PI / 180;
    latB *= Math.PI / 180;
    lonA *= Math.PI / 180;
    lonB *= Math.PI / 180;
    let deltaLon = lonB - lonA;
    let numerator = Math.sqrt( Math.pow(Math.cos(latB) * Math.sin(deltaLon), 2) + Math.pow(Math.cos(latA) * Math.sin(latB) - Math.sin(latA) * Math.cos(latB) * Math.cos(deltaLon), 2));
    let denominator = Math.sin(latA) * Math.sin(latB) + Math.cos(latA) * Math.cos(latB) * Math.cos(deltaLon);
    let delta = Math.atan2(numerator, denominator);
    return EARTH_RADIUS * delta;
}