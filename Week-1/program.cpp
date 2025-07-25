#include <bits/stdc++.h>
using namespace std;

void program1(int num1, int num2){
    int sum = num1 + num2;
    cout << "The sum of " << num1 << " and " << num2 << " is: " << sum << endl;
    cout << "This is the first program." << endl;
}
void program2(int arr[], int size){
    cout << "The elements of the array are: ";
    for(int i = 0; i < size; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
    cout << "This is the second program." << endl;
}

int main(){
    // Program 1
    int num1, num2;
    cout << "Enter two integers for Program 1: ";
    cin >> num1 >> num2;
    program1(num1, num2);
    // Program 2
    int size;
    cout << "Enter the size of the array for Program 2: ";
    cin >> size;
    int arr[size];
    program2(arr, size);
    return 0;
}