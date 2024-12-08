/*
������ �3

�� ����� Python ��� �++ ���������� ��������, ������� ������� ����� (�� ������������ �����) ����������� ������ �� ������ �����.
������ ����� ���� ������ ������� �� ��������� �������� ����� (� ��� ����� � ���������������).
���������, ������ �� ��������, ��� ������� ������������� �������� ���������.
*/

/*
������ � ����� ��� ��������� Timsort, �� � ����������� ���������� ���������� ����������, ��� ��� �����
�������� ����� �����������, �� �� ��� �������, ���������� � ������� ���������� ��������.
*/


#include <iostream>
#include <vector>


void merge_sort(std::vector<int>& arr, int left, int right) {
    if (left >= right) return;
    int mid = (left + right) / 2;
    merge_sort(arr, left, mid);
    merge_sort(arr, mid + 1, right);

    std::vector<int> temp;
    int i = left;
    int j = mid + 1;


    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp.push_back(arr[i]);
            i++;
        }
        else {
            temp.push_back(arr[j]);
            j++;
        }
    }

    while (i <= mid) {
        temp.push_back(arr[i]);
        i++;
    }

    while (j <= right) {
        temp.push_back(arr[j]);
        j++;
    }

    for (i = left; i <= right; i++) {
        arr[i] = temp[i - left];
    }
}

int main()
{

}

