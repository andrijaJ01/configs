#!/bin/bash


export AMO_JWT_SECRET=5e65bca668e1167ab83c2952881ceec1fd69fee6e600f8da502f27
export AMO_JWT_ISSUER=user:15094280:630

cp -rv $HOME/.cache/wal/colors.css .

web-ext sign --api-key=$AMO_JWT_ISSUER --api-secret=$AMO_JWT_SECRET

clear
dunstify "FINISHED MAKING EXTENSION"
