def backupUpdate(backup, lst):
    '''
    Backups the current list of complex numbers.
    :param backup: Backup list.
    :param lst: List of complex numbers.
    :return: Updated backup list.
    '''
    backup.append([dict(item) for item in lst])
    return backup


def undo(backup, lst, original_lst):
    '''
    Undoes the last modification of the list of complex numbers.
    :param backup: Backup list.
    :param lst: List of complex numbers.
    :param original_lst: The original list of complex numbers that was read at the start of the program.
    '''
    if backup:
        backup.pop()
        try:
            last_backup = backup[-1]
            lst.clear()
            lst.extend(last_backup)
        except IndexError:
            lst.clear()
            lst.extend(original_lst)
    else:
        lst.clear()
        lst.extend(original_lst)

    return lst