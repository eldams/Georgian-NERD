#include <fstream>
#include <string>
#include <set>
#include <array>
#include <ctime>
#include <algorithm>

using namespace std;

void generate_random_lines(set<long long>&s,long long numOfLines){
	++numOfLines;
	srand(time(NULL));
	while(s.size() != 1000){
		s.insert(rand() % numOfLines);
	}
}

long long count_lines(const string fileName){
	ifstream ifs(fileName);
	string s;
	long long count =0;
	while(getline(ifs,s)){
		count++;
	}
	ifs.close();
	return count;
}
void read_file_fill_data_array(set<long long>&s,array<string,1000>&data,const string fileName){
	ifstream ifs(fileName);
	long long currentLineNum = 1;
	int dataIndex=0;
	string lineOfData;
	for(set<long long>::iterator it = s.begin();it!=s.end();++it){
		for(currentLineNum;currentLineNum<(*it);++currentLineNum){
			getline(ifs,lineOfData);
		}
		getline(ifs,lineOfData);
		++currentLineNum;
		data[dataIndex++] = lineOfData;
	}
	ifs.close();
}
void generate_output_files(const array<string,1000>&data,const string outFileDir){
	int currentOutFileIndex = 1;
	ofstream ofs(outFileDir + to_string(currentOutFileIndex) + ".txt");
	for(int i=0;i<data.size();i++){
		ofs << data[i] << endl;
		if((i+1)%10 == 0){
			ofs.close();
			currentOutFileIndex++;
			ofs.open(outFileDir + to_string(currentOutFileIndex) + ".txt");
		}
	}
	ofs.close();
}
int main(){
	srand(time(NULL));
	const string inputFileName = "data/all.txt";
	const string outputDir = "data/splitted/";

	set<long long> s;
	array<string,1000> data;
	
	generate_random_lines(s,count_lines(inputFileName));
	
	read_file_fill_data_array(s,data,inputFileName);
	
	random_shuffle(data.begin(),data.end());
	
	generate_output_files(data,outputDir);
	
	return 0;
}
