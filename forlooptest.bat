@echo off

SETLOCAL
setlocal EnableDelayedExpansion
SET "prefix=prefix/"
SET "var1=val1 val2 val3 var4"
SET "var2="
FOR  %%A IN (%var1%) DO (
        SET "var2=!var2! %prefix%%%A"
        echo !var2!
        )

echo %var2%

