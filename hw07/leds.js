#!/usr/bin/env node
// Blinks various LEDs
const Blynk = require('blynk-library');
const b = require('bonescript');
const util = require('util');

const LED0 = 'USR3';
const LED1 = 'P9_14';
b.pinMode(LED0, b.OUTPUT);
b.pinMode(LED1, b.ANALOG_OUTPUT);

const AUTH = 'xKOrQO_5UjP1IVxbF98LvlW7itaLGUCZ';

var blynk = new Blynk.Blynk(AUTH);

var v0 = new blynk.VirtualPin(0);
var v1 = new blynk.VirtualPin(1);
// var v10 = new blynk.WidgetLED(10);

v0.on('write', function(param) {
    console.log('V0:', param[0]);
    b.digitalWrite(LED0, param[0]);
});

v1.on('write', function(param) {
    var value = param[0]/1023;
    console.log('V1 this file:', value);
    b.analogWrite(LED1, value);
});