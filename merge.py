def merge_sort(data, draw):
    # MERGE SORT (top-down) #

    mergesort(A as list)
       if length(A) == 1 then return A

        left ← A[0]..A[length(A)/2]
        right ← A[length(A)/2]..A[length(A)-1]

        left ← mergesort(left)
        right ← mergesort(right)

        return merge(left, right)
    end func

    merge(A as list, B as list):
        C ← []

        while length(A) > 0 and length(B) > 0
           if A[0] > B[0] then
               add B[0] to the end of C
                remove B[0] from B
            else
               add A[0] to the end of C
                remove A[0] from A
            end if
        end while
        while length(A) > 0
           add A[0] to the end of C
            remove A[0] from A
        end while
        while length(B) > 0
           add B[0] to the end of C
            remove B[0] from B
        end while
        return C
    end func
