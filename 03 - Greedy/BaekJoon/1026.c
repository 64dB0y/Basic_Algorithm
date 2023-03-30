#include <stdio.h>

int main(void){
    int n;  // 최대 몇개의 수를 입력할 것인가
    scanf_s("%d",&n);
    int arr1[n];
    int arr2[n];
    for (int i = 0; i<n; i++){
        scanf_s("%d", &arr1[i]);
    }
    for (int i = 0; i<n; i++){
        scanf_s("%d", &arr2[i]);
    }

    // arr1을 버블 정렬
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr1[j] > arr1[j + 1]) {
                int temp = arr1[j];
                arr1[j] = arr1[j + 1];
                arr1[j + 1] = temp;
            }
        }
    }

    // arr1의 최솟값과 arr2의 최솟값을 곱해서 누적한 결과를 출력
    int result = 0;
    for (int i = 0; i < n; i++) {
        int min_val = arr1[i] * arr2[0]; // arr1[i]와 arr2[0]을 곱한 값이 최솟값이라고 가정
        for (int j = 0; j < n; j++) {
            if (arr1[i] * arr2[j] < min_val) {
                min_val = arr1[i] * arr2[j];
            }
        }
        result += min_val;
    }

    printf("%d\n", result);
    return 0;
}