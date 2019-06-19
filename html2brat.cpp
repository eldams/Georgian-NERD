#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Anotation{
	long long B,E;
	string Value,Tag;
};
Anotation process_tag(string tag){
	Anotation tempAno;
	int greatInd=-1;
	int quoteInd=-1;
	for(size_t i=1;i<tag.size()-1;i++){
		if(quoteInd != -2){
			if(tag[i] == '"' && quoteInd == -1) quoteInd = i+1;
			else if(tag[i] == '"') {tempAno.Tag = tag.substr(quoteInd,i-quoteInd); quoteInd = -2;}
		}
		if(tag[i] == '>') greatInd=i+1;
		else if(tag[i] == '<') {tempAno.Value = tag.substr(greatInd,i-greatInd); i=tag.size();}
	}
	return tempAno;
}
pair<string,vector<Anotation>> process_line(string & Line,long long lastLineIndex){
	pair<string,vector<Anotation>> ret;
	int p=-1;
	int count = 0;
	for(size_t i=0;i<Line.size();i++){
		if(Line[i] == '<' && p==-1) p=i+1;
		else if(Line[i] == '>' && !count) count++;
		else if(Line[i] == '>'){
			Anotation tempAno = process_tag(Line.substr(p,p-i));
			Line = Line.replace(p-1,i-p+2,tempAno.Value);
			tempAno.B = p-1+lastLineIndex;
			tempAno.E = p-1+tempAno.Value.size()-1+lastLineIndex;
			ret.second.push_back(tempAno);
			i=p-1 + tempAno.Value.size()-1;
			p=-1;
			count = 0;
		}
	}
	ret.first = Line;
	return ret;
}
void write_data_n_anot(const pair<string,vector<Anotation>>&DataNAnot,const string&AnotOut,const string&DataOut){
	ofstream ofs(DataOut,fstream::app);
	ofs << DataNAnot.first << endl;
	ofs.close();
	ofs.open(AnotOut,fstream::app);
	for(Anotation i: DataNAnot.second){
		ofs << i.B << ' ' << i.E << ' ' << i.Tag << ' ' << i.Value << endl;
	}
	ofs.close();
}
void clear_out_files(const string & AnotOut,const string&DataOut){
	ofstream ofs(AnotOut);
	ofs << "";
	ofs.close();
	ofs.open(DataOut);
	ofs << "";
	ofs.close();
}
void process_n_write(const string&DataInp,const string&AnotOut,const string&DataOut){
	ifstream ifs(DataInp);
	string Line;
	long long LineIndex=0;
	clear_out_files(AnotOut,DataOut);
	while(getline(ifs,Line)){
		pair<string,vector<Anotation>> DataNAnot = process_line(Line,LineIndex);
		write_data_n_anot(DataNAnot,AnotOut,DataOut);
		LineIndex+=Line.size();
	}
	ifs.close();
}

int main(){
	const string fileName = "inp.txt";
	const string anotationOutFileName = "ann.txt";
	const string dataOutFileName = "data.txt";
	process_n_write(fileName,anotationOutFileName,dataOutFileName);
}
