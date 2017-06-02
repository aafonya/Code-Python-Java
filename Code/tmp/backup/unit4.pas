program project2;

{$mode objfpc}{$H+}

uses
  {$IFDEF UNIX}{$IFDEF UseCThreads}
  cthreads,
  {$ENDIF}{$ENDIF}
  Classes
  { you can add units after this };

{$R *.res}

const N=100000;
const p=0.7;
const q=1-p;


var populacio:array[1..N] of array [1..2]of char;
populacio2:array[1..N] of array [1..2]of char;
i,a,b,x,y,w,z,s:integer;



begin
  randomize;
  for i:=1 to N do
  begin
  if random<=p then populacio[i,1]:='A' else populacio[i,1]:='a';
  if random<=p then populacio[i,2]:='A' else populacio[i,2]:='a';

  end;

  a:=0;
  b:=0;
  for i:=1 to N do
  begin
  if (populacio[i,1]='A') and (populacio[i,2]='A') then a:=a+1;
  if (populacio[i,1]='a') and (populacio[i,2]='a') then b:=b+1;

  end;
  writeln(a);
  writeln(b);
  writeln(N-a-b);


for s:=1 to 500 do
begin
  for i:=1 to N do
  begin
    x:=random(100)+1;
    z:=random(2)+1;
    y:=random(100)+1;
    w:=random(2)+1;
    populacio2[i,1]:=populacio[x,z];
    populacio2[i,2]:=populacio[y,w];
  end;
  populacio:=populacio2;

  a:=0;
  b:=0;
  for i:=1 to N do
  begin
  if (populacio[i,1]='A') and (populacio[i,2]='A') then a:=a+1;
  if (populacio[i,1]='a') and (populacio[i,2]='a') then b:=b+1;

  end;
  writeln(a,' ',b,' ',N-a-b);

  end;
readln();
end.







end.



