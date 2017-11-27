CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(50),
    IN p_SID VARCHAR(50),
    IN p_role VARCHAR(50),
    IN p_marker VARCHAR(50)
)
BEGIN
    if ( select exists (select 1 from tbl_user where user_SID = p_SID) ) THEN
     
        select 'SID already Registered !!';
     
    ELSE
     
        insert into tbl_user
        (
            user_name,
            user_SID,
            user_role,
            user_marker
        )
        values
        (
            p_name,
            p_SID,
            p_role,
            p_marker
        );
     
    END IF;
END