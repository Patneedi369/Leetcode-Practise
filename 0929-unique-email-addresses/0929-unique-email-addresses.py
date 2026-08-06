class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            
            # Truncate local name at the first '+' if present
            local = local.split('+')[0]
            
            # Remove all '.' characters from local name
            local = local.replace('.', '')
            
            # Reconstruct and add to the set
            unique_emails.add(f"{local}@{domain}")
            
        return len(unique_emails)