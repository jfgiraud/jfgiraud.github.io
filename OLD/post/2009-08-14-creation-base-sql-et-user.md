---
layout: post
title: "Creation base sql et user"
date: "2009-08-14 11:00:00"
---
create database mabase;
grant all privileges on mabase.* to test identified by 'test';
mysql -h localhost -u test -ptest mabase
