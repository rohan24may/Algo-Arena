void deleteElement(int arr[], int &n, int position)
{
    for(int i = position; i < n - 1; i++)
    {
        arr[i] = arr[i + 1];
    }

    n--;
}
void reverseArray(int arr[], int n)
{
    int left = 0;
    int right = n - 1;

    while(left < right)
    {
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;

        left++;
        right--;
    }
}

void removeDuplicates(int arr[], int &n)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = i + 1; j < n; j++)
        {
            if(arr[i] == arr[j])
            {
                for(int k = j; k < n - 1; k++)
                {
                    arr[k] = arr[k + 1];
                }

                n--;
                j--;
            }
        }
    }
}
void leftRotate(int arr[], int n, int k)
{
    for(int r = 0; r < k; r++)
    {
        int temp = arr[0];

        for(int i = 0; i < n - 1; i++)
        {
            arr[i] = arr[i + 1];
        }

        arr[n - 1] = temp;
    }
}
void rightRotate(int arr[], int n, int k)
{
    for(int r = 0; r < k; r++)
    {
        int temp = arr[n - 1];

        for(int i = n - 1; i > 0; i--)
        {
            arr[i] = arr[i - 1];
        }

        arr[0] = temp;
    }
}