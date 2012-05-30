/*======================================================================*
 * Copyright (c) 2008, Yahoo! Inc. All rights reserved.                 *
 *                                                                      *
 * Licensed under the New BSD License (the "License"); you may not use  *
 * this file except in compliance with the License.  Unless required    *
 * by applicable law or agreed to in writing, software distributed      *
 * under the License is distributed on an "AS IS" BASIS, WITHOUT        *
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.     *
 * See the License for the specific language governing permissions and  *
 * limitations under the License. See accompanying LICENSE file.        *
 *======================================================================*/
#ifndef __M_MEM_H__
#define __M_MEM_H__

/*! \file m_mem.h
 *  \brief Memory management routines.  Some prototypes are copied from glib,
 *         but we don't link to glib in case a user doesn't want to have to
 *         link to glib in their program.
 */

#include <stdlib.h>

/*! \fn m_try_malloc(size_t size)
 *  \brief  Attempd to allocate size bytes, and return NULL on failure.  Does
 *          not initialize the memory.
 *  \param  size number of bytes to allocate
 *  \return the allocated memory, or NULL
 */
void *m_try_malloc(size_t size);

/*! \fn m_try_malloc0(size_t size)
 *  \brief  Attempt to allocate size bytes, initialized to 0's, and return
 *          NULL on failure.
 *  \param  size number of bytes to allocate
 *  \return the allocated memory, or NULL
 */
void *m_try_malloc0(size_t size);

/*! \fn m_try_realloc(void *ptr, size_t size)
 *  \brief reallocate memory, the new memory is uninitialized.
 */
void *m_try_realloc(void *ptr, size_t size);

/*! \fn m_free(void *ptr)
 *  \brief Free the memory referenced by ptr.  If ptr is NULL, no operation
 *         is performed.
 *  \param ptr pointer to memory
 */
void m_free(void *ptr);

#endif

