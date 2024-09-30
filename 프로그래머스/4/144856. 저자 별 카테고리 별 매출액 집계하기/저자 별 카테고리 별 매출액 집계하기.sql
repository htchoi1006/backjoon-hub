SELECT A.AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(SALES * PRICE) TOTAL_SALES
FROM BOOK A 
JOIN AUTHOR B ON A.AUTHOR_ID = B.AUTHOR_ID
JOIN BOOK_SALES C ON A.BOOK_ID = C.BOOK_ID
WHERE SALES_DATE LIKE '2022-01%'
GROUP BY A.AUTHOR_ID, CATEGORY
ORDER BY A.AUTHOR_ID, CATEGORY DESC